from flask import render_template
from app.main import bp
from flask import jsonify, request, abort

from app.main.functions import (
    combine_letters,
    check_word,
    wordle_solver,
    combine_results,
)


@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@bp.route("/api/validate_word", methods=["POST"])
def validate_word():
    word_list = request.get_json() or {}
    recent_word = combine_letters(word_list[-1])
    if not check_word(recent_word):
        return jsonify({"error": "Not a word"}), 400


@bp.route("/api/process_words", methods=["POST"])
def process_words():
    word_list = request.get_json() or {}
    recent_word = combine_letters(word_list[-1])
    recent_result = combine_results(word_list[-1])
    suggested_word = wordle_solver(recent_word, recent_result)
    response = jsonify(suggested_word)
    response.status_code = 201
    return response
