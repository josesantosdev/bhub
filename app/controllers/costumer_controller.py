from flask import Blueprint, json, Response, request

from app import db

from app.models.costumer_model import Costumer, CostumerSchema


class CostumerController(object):

    costumer_controller = Blueprint('costumer_controller', __name__)

    @costumer_controller.route('/cadastrar', methods=['POST'])
    def create_costumer():
        request_data = request.get_json()
        costumer_schema = CostumerSchema()

        try:
            costumer = costumer_schema.load(request_data)
        except:
            return custom_response({"error": "Consult documentation to create a new costumer"}, 401)

        return custom_response(costumer_schema.dump(costumer.save()), 201)

    @costumer_controller.route('/consultar', methods=['GET'])
    def get_costumer():
        costumer_list = Costumer.query.all()
        costumer_schema = CostumerSchema(many=True)
        return custom_response(costumer_schema.dump(costumer_list), 200)

    @costumer_controller.route('/consultar/<id_cliente>', methods=['GET'])
    def get_costumer_by_id(id_cliente):
        try:
            costumer = Costumer.query.filter_by(id_cliente=id_cliente).first_or_404()
        except:
            return custom_response('Costumer not found', 404)

        costumer_schema = CostumerSchema()
        return custom_response(costumer_schema.dump(costumer), 200)

    @costumer_controller.route('/atualizar/<id_cliente>', methods=['PUT'])
    def update_costumer(id_cliente):
        costumer_schema = CostumerSchema()

        try:
            costumer = Costumer.query.filter(Costumer.id_cliente == id_cliente).first_or_404()
        except:   
            return custom_response('Costumer not found', 404)
        
        query = Costumer.query.filter(Costumer.id_cliente == id_cliente)
        query.update(request.get_json())
        return custom_response(costumer_schema.dump(query.first()), 201)

    @costumer_controller.route('/deletar/<id_cliente>', methods=['DELETE'])
    def delete_costumer(id_cliente):
        try:
            costumer = Costumer.query.filter(Costumer.id_cliente == id_cliente).first_or_404()
        except:
            return custom_response('Costumer not found', 404)

        costumer.delete()
        db.session.commit()
        return custom_response('Deleted', 201)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
