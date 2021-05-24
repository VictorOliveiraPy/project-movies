# app/tests/movies/test_models.py

import pytest

from movies.models import Movie


@pytest.mark.django_db
def test_movie_model():
    movie = Movie(title="Raising Arizona", genre="comedy", year="1987")
    movie.save()
    assert movie.title == "Raising Arizona"
    assert movie.genre == "comedy"
    assert movie.year == "1987"
    assert movie.created_date
    assert movie.updated_date
    assert str(movie) == movie.title


@pytest.mark.django_db
def test_add_movie_invalid_json(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        "/api/movies/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400

    movies = Movie.objects.all()
    assert len(movies) == 0


@pytest.mark.django_db
def test_add_movie_invalid_json_keys(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        "/api/movies/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    movies = Movie.objects.all()
    assert len(movies) == 0