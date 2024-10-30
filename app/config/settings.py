from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    oauth2_token_uri: str = "http://keycloak:8080/realms/streaming/protocol/openid-connect/token"
    oauth2_client_id: str = "streaming"
    oauth2_client_secret: str = "APpAVE2mJ3RF53ELVmzXmf7oABUKqwHK"

                         # postgresql://<username>:<password>@<host>:<port>/<database>
    postgresql_url: str = "postgresql://postgres:***@host.docker.internal:5432/postgres"

    service_endpoint_filme_getall: str = "http://filme:8080/filme"