import pandas as pd

# carrega um arquivo do tipo json
df = pd.read_json("D:\Python\SoulOn-Python3\Modulo2\dados_json.json")

print(df.to_string())

# carrega uma variavel com um formata de arquivo json
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409.1,
    "1":479.0,
    "2":340.0,
    "3":282.4,
    "4":406.0,
    "5":300.5
  }
}

# converte a variavel em um DF
df = pd.DataFrame(data)

# printa da tela o conteudo da variavel
print(df)
