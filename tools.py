import sys
from datetime import datetime

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain.chat_models import init_chat_model


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


@tool
def time_now():
    """
    que horas
    que horas sao
    que horas são?
    Por favor, que horas são?
    Por favor teria horas?
    Você tem horário?
    """
    print('-' * 40)
    print(f'DEBUG: time_now()')
    print('-' * 40)
    now = datetime.now()
    return f'Agora são {now}'


@tool
def get_tch(id_talhao: str):
    """
    qual o TCH do Talhão "id_talhao"
    qual a quantidade colhida no Talhão "id_talhao" na ultima safra
    """
    print('-' * 40)
    print(f'DEBUG: get_tch({id_talhao})')
    print('-' * 40)
    tch = 999
    return f'O TCH do talhão "{id_talhao}" é {tch}'


@tool
def set_vehicle_fuel(quantidade_em_litros: int, id_veiculo: str):
    """
    registrar abastecimento de QUANTIDADE_EM_LITROS na ID_VEICULO
    anotar abastecimento de QUANTIDADE_EM_LITROS em ID_VEICULO
    marcar abastecimento de QUANTIDADE_EM_LITROS ID_VEICULO
    guardar abastecimento de QUANTIDADE_EM_LITROS ID_VEICULO
    salvar abastecimento de QUANTIDADE_EM_LITROS ID_VEICULO
    """
    print('-' * 40)
    print(f'DEBUG: set_vehicle_fuel({quantidade_em_litros},{id_veiculo})')
    print('-' * 40)
    return f'Abastecimento de {quantidade_em_litros}L do veículo "{id_veiculo}" registrado'


TOOLS_DICT = {
    # 'MULTIPLY': multiply,
    # 'TIME_NOW': time_now,
    'SET_VEHICLE_FUEL': set_vehicle_fuel,
    'GET_TCH': get_tch,
}


# llm = init_chat_model('granite3.3:2b', model_provider='ollama')
# llm = init_chat_model('llama3.2:1b', model_provider='ollama', temperature=0.0)
llm = init_chat_model('qwen2.5:0.5b', model_provider='ollama', temperature=0.0)


llm_with_tools = llm.bind_tools(list(TOOLS_DICT.values()))

# query = 'What is 3 * 12?'
query = sys.argv[1]
print(query)

messages = [HumanMessage(query)]

ai_msg = llm_with_tools.invoke(messages)

messages.append(ai_msg)


first_tool_msg = None

for tool_call in ai_msg.tool_calls:
    tool_name = tool_call['name'].upper()
    selected_tool = TOOLS_DICT[tool_name]
    tool_msg = selected_tool.invoke(tool_call)
    if not first_tool_msg:
        first_tool_msg = tool_msg
    # print(tool_msg)
    messages.append(tool_msg)


# print(llm_with_tools.invoke(messages).content)
if first_tool_msg:
    print('=' * 40)
    print(first_tool_msg.content)
else:
    print(messages)
# print('-' * 40)
# print(messages)
# print('-' * 40)
# print(messages[0])
# print(messages[-1])
# print('=' * 40)
# print(messages[-1].content)
# print('=' * 40)
