from app.domain.interfaces.entities.ishopping_repository import ShoppingRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_internal_error, response_ok
from app.presentation.schemas.response_schema import SchemaResponseHttp


class FindShoppingIdUseCase(UseCaseInterface):
    def __init__(self, shopping_repository: ShoppingRepositoryInterface):
        self.__shopping_repository = shopping_repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            shopping = self.__shopping_repository.find_by_id(params)

            if not shopping:
                return response_not_found("Compra não encontrada")

            return response_ok(
                "Compra encontrada com sucesso",
                {
                    "shopping_id": shopping.get_shopping_id(),
                    "product_id": shopping.get_product_id(),
                    "supplier_id": shopping.get_supplier_id(),
                    "quantity": shopping.get_quantity(),
                    "price_cost": shopping.get_price_cost(),
                    "created_at": shopping.get_created_at()
                }
            )
        except:
            return response_internal_error("Erro inesperado ao buscar a compra.")

