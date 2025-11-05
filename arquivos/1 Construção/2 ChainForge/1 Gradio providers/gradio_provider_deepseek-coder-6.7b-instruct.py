# --------------------------------------------------
# CUSTOM PROVIDER PARA USO NO CHAINFORGE
# MODEL: "deepseek-coder-6.7b-instruct"
# --------------------------------------------------

from chainforge.providers import provider
from gradio_client import Client

# Link do Gradio gerado no Colab
GRADIO_URL = ""
client = Client(GRADIO_URL)

# Schema de configuração
GRADIO_SETTINGS_SCHEMA = {
  "settings": {
    "max_tokens": {
      "type": "integer",
      "title": "max_tokens",
      "description": "Máximo de tokens a gerar",
      "default": 150,
      "minimum": 1,
      "maximum": 2048
    },
  },
  "ui": {
    "max_tokens": {
      "ui:help": "Número máximo de tokens",
      "ui:widget": "range"
    }
  }
}

@provider(
    name="DeepSeekCoder-6.7b",
    emoji="🔗",
    models=["default"],
    rate_limit="sequential",
    settings_schema=GRADIO_SETTINGS_SCHEMA
)
def GradioCompletion(prompt: str, model: str = "default", max_tokens: int = 150, **kwargs) -> str:
    """
    Provider customizado que envia o prompt para um endpoint Gradio (Colab).
    """
    try:
        result = client.predict(prompt)

        if isinstance(result, (list, tuple)):
            return str(result[0])
        return str(result)

    except Exception as e:
        return f"Erro ao chamar Gradio: {e}"