# Tabla lógica
Daniela Ortiz:
- Alta
- Pelo largo

## And (y)
| A | B | Resultado | Ejemplo |
|---|---|-----------|---------|
| 0 | 0 | 0         |Maria es baja (Falso) y tiene pelo corto (Falso) = Falso|
| 0 | 1 | 0         |Maria es baja (Falso) y tiene pelo largo (Verdadero) = Falso|
| 1 | 0 | 0         |Maria es alta (Verdadero) y tiene pelo corto (Falso) = Falso|
| 1 | 1 | 1         |Maria es alta (Verdadero) y tiene pelo largo (Verdadero) = Verdadero|

## Or (o)
| A | B | Resultado | Ejemplo |
|---|---|-----------|-------|
| 0 | 0 | 0         |Maria es baja (Falso) o tiene pelo corto (Falso) = Falso|
| 0 | 1 | 1         |Maria es baja (Falso) o tiene pelo largo (Verdadero) = Verdadero|
| 1 | 0 | 1         |Maria es alta (Verdadero) o tiene pelo corto (Falso) = Verdadero|
| 1 | 1 | 1         |Maria es alta (Verdadero) o tiene pelo largo (Verdadero) = Verdadero|

## Not (no)
| A | Resultado |
|---|-----------|
| 0 | 1         |
| 1 | 0         |


# 10 == 8             -> False
# 1 != 2               -> True
# 4 > 4                -> False
# 7 < 7                -> False
# 4 >= 4               -> True
# 7 <= 7               -> True