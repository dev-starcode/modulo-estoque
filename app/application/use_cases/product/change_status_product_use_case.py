from app.domain.interfaces.entities.iproduct_repository import ProductRepositoryInterface
from app.domain.interfaces.use_case.use_case_interface import UseCaseInterface
from app.presentation.http.response import response_not_found, response_ok
from app.presentation.schemas.response_schema import SchemaResponseHttp


class ChangeStatusProductUseCase(UseCaseInterface):
    def __init__(self, product_repository: ProductRepositoryInterface):
        self.__product_repository = product_repository

    def execute(self, params: dict = None) -> SchemaResponseHttp:
        try:
            product = self.__product_repository.change_status_product(params)

            if not product:
                return response_not_found("Produto não encontrado")

            return response_ok(
                "Status do produto alterado com sucesso",
                None
            )

        except:
            return response_internal_error("Erro ao tentar alterar estado do produto.")