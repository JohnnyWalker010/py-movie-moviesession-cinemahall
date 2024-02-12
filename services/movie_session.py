from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall
from datetime import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(session_date=None) -> QuerySet[MovieSession]:
    query_set = MovieSession.objects.all()
    if session_date:
        query_set = query_set.filter(show_time__date=session_date)
    return query_set


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> MovieSession:
    current_session = MovieSession.objects.get(id=session_id)
    if show_time:
        current_session.show_time = show_time
    if movie_id:
        current_session.movie_id = movie_id
    if cinema_hall_id:
        current_session.cinema_hall_id = cinema_hall_id

    current_session.save()
    return current_session


def delete_movie_session_by_id(session_id):
    MovieSession.objects.get(id=session_id).delete()