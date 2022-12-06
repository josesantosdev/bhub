from flask import Blueprint, json, Response, request

from app import db

from app.models.bank_details_model import BankDetail, BankDetailSchema


class BankDetailsController(object):

    bank_controller = Blueprint('bank_controller', __name__)

    @bank_controller.route('/cadastrar', methods=['POST'])
    def create_bank_account():
        request_data = request.get_json()
        bank_schema = BankDetailSchema()

        try:
            bank_detail = bank_schema.load(request_data)
        except:
            return custom_response({"error": "Consult documentation to create a new bank account for costumer"}, 401)

        return custom_response(bank_schema.dump(bank_detail.save()), 201)


    @bank_controller.route('/deletar/<id_conta_banco>', methods=['DELETE'])
    def delete_bank_account(id_conta_banco):
        try:
            bank_detail = BankDetail.query.filter(BankDetail.id_conta_banco == id_conta_banco).first_or_404()
        except:
            return custom_response('Bank Account not found', 404)

        bank_detail.delete()
        db.session.commit()
        return custom_response('Deleted', 201)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )