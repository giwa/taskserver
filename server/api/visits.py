from flask import Blueprint, request, abort

from server import di
from server.util import mjsonify

cxt = di.cxt
visit_bp = Blueprint('visit_api', __name__)


@visit_bp.route("", methods=["GET"])
def get_visits():
    visits = cxt.dao.visit.get_list()
    rs = cxt.scheme.visits.dump(visits).data
    return mjsonify(rs)


@visit_bp.route("/<int:id>", methods=["GET"])
def get_visit(id):
    visit = cxt.dao.visit.get_by_id(id)
    rs = cxt.scheme.visit.dump(visit).data
    return mjsonify(rs)

