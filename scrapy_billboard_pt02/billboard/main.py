from billboard import crawler
import streamlit as st
import pandas as pd
import altair as alt
from altair import Axis

# from time import sleep


def get_years_from_decade(decade):
    match decade:
        case (1950):
            return 1959, 1959
        case (1960):
            return 1960, 1969
        case (1970):
            return 1970, 1979
        case (1980):
            return 1980, 1989
        case (1990):
            return 1990, 1999
        case (2000):
            return 2000, 2009
        case (2010):
            return 2010, 2019
        case (2020):
            return 2020, 2023
        case _:
            return 1959, 2023


def clear_decade_year():
    st.session_state.decade = None
    st.session_state.selected_year = None

def set_interval_from_year():
    if st.session_state.selected_year is not None:
        st.session_state.years = (st.session_state.selected_year, st.session_state.selected_year)
    else:
        st.session_state.years = (1959,2023)
    st.session_state.decade = None
def set_years_from_decade():
    st.session_state.years = get_years_from_decade(st.session_state.decade)
    st.session_state.selected_year = None

def get_top10_artists_by_weeks(grouped):
    return grouped[["date"]].count().sort_values(by="date", ascending=False)[0:10]


def get_top10_artists_by_song(grouped):
    return grouped["song"].nunique().sort_values(by="song", ascending=False)[0:10]


def get_top_10_songs_by_number_of_weeks(df):
    df_group_by_song = df.groupby(["artist", "song"], as_index=False)
    df_count = df_group_by_song.count()
    df_count["song_artist"] = df_count.apply(lambda row: row.song + " - " + row.artist.upper(), axis=1)
    return df_count.sort_values(by="date", ascending=False)[0:10]


def display_graphics(df, filtered_by_artist):
    if not filtered_by_artist:
        st.subheader("Ranking dos artistas que mais figuraram no topo da parada")
        df_grouped_artist = df.groupby("artist", as_index=False)
        st.markdown("#### Por número de semanas")
        st.write(alt.Chart(
            get_top10_artists_by_weeks(df_grouped_artist),
        ).mark_bar().encode(
            y=alt.Y("artist:N", axis=Axis(title='Artista')).sort("-x"),
            x=alt.X('date:Q', axis=Axis(title="Total de semanas em 1º lugar")),
            tooltip=[
                alt.Tooltip("artist", title="Artista:"),
                alt.Tooltip("date", title="Total de semanas em 1ºlugar:")
            ]
        ))
        # st.bar_chart(get_top10_artists_by_weeks(df_grouped_artist), horizontal=True)
        st.markdown("#### Por número de músicas")
        st.write(alt.Chart(
            get_top10_artists_by_song(df_grouped_artist),
        ).mark_bar().encode(
            y=alt.Y("artist:N", axis=Axis(title='Artista')).sort("-x"),
            x=alt.X('song:Q', axis=Axis(title='Quantidade de Músicas')),
            tooltip=[
                alt.Tooltip("artist", title="Artista:"),
                alt.Tooltip("song", title="Qtde. de músicas:"),
            ]
        ))

    # st.bar_chart(get_top10_artists_by_song(df_grouped_artist), horizontal=True)
    st.subheader("As músicas que mais tempo permaneceram em primeiro lugar ")
    st.write(alt.Chart(
        get_top_10_songs_by_number_of_weeks(df),
    ).mark_bar().encode(
        y=alt.Y("song_artist:N", axis=Axis(title="Música")).sort("-x"),
        x=alt.X('date:Q', axis=Axis(title="Total de semanas em 1º lugar", tickMinStep=1)),
        tooltip=[
            alt.Tooltip("artist", title="Artista:"),
            alt.Tooltip("song", title="Música:"),
            alt.Tooltip("date", title="Total de semanas em 1ºlugar:")
        ]

    ))


def load_panel():
    st.title("Billboard Hot 100")
    st.header("Exibindo lista de músicas que atingiram o topo da parada Billboard Hot 100")
    data_load_state = st.text('Carregando dados...')
    # get_data()
    df = pd.read_json('items.json')
    df["link_chart"] = df.apply(lambda row: f"https://www.billboard.com/charts/hot-100/{row.date:%Y-%m-%d}", axis=1)
    # <editor-fold desc="Sidebar">
    st.sidebar.header("Filtros")
    st.sidebar.subheader("Filtro por ano")
    st.sidebar.number_input("Ano:",value=None, key="selected_year",min_value=1959, max_value=2023, step=1, on_change=set_interval_from_year)
    st.sidebar.subheader("Filtro por período")
    st.sidebar.slider('Selecione o período desejado', 1959, 2023, (1959, 2023), key="years",
                      on_change=clear_decade_year)
    st.sidebar.subheader("Ou")
    st.sidebar.subheader("Filtro por década")
    st.sidebar.selectbox("Década", range(1950, 2030, 10), index=None, key="decade", on_change=set_years_from_decade)
    # </editor-fold>

    # <editor-fold desc="Filter">

    # </editor-fold>
    # <editor-fold desc="Data">
    (min_year, max_year) = st.session_state.years
    filtered_df = df[(df["year"] >= min_year) & (df["year"] <= max_year)]
    artists = sorted(filtered_df["artist"].unique())
    st.sidebar.subheader("Filtro por artista")
    st.sidebar.selectbox("Artista", artists, index=None, key="artist")
    if "artist" in st.session_state.keys() and st.session_state.artist:
        filtered_df = filtered_df[filtered_df["artist"] == st.session_state.artist]
        is_filtered_by_artist = True
    else:
        is_filtered_by_artist = False
    st.dataframe(filtered_df,
                 column_config={"sequential_no": "Sequencial",
                                "date": st.column_config.DateColumn(
                                    "Data", format="DD/MM/YYYY"),
                                "song": "Música",
                                "artist": "Artista",
                                "year": st.column_config.NumberColumn(
                                    "Ano", format="%d"),
                                "link_chart": st.column_config.LinkColumn(
                                    "Referência", help="Link p/ a página da Billboard",
                                    display_text="Ir p/ parada")
                                },
                 hide_index=True
                 )

    data_load_state.info(f"{filtered_df.shape[0]} registro(s) carregado(s)")
    display_graphics(filtered_df, is_filtered_by_artist)
    # </editor-fold>


@st.cache_data
def get_data():
    crawler.start_crawler()


if __name__ == '__main__':
    load_panel()
    # get_data()
