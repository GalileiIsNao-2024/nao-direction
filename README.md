# nao-direction

**Dati di input**:
```json
{
    "signal_code": /* string */,
    "product_name": /* string */
}
```
- `signal_code` codice restituito dal Nao Mark
- `product_name` nome del prodotto scento dall'utente 

**Dati di output**:
`direction` direzione in cui si può trovare l'elemento.

Struttura output:
- `right`, `front`, `left` l'elemento si trova nelle diramazioni delle corsie corrispondenti
- `to_right`, `to_front`, `to_left` l'elemento si trova nella corsia corrispondente


## Description

Il raspberry riceve un codice tramite il [socket](https://github.com/GalileiIsNao-2024/socket) che va a ricercare all'interno del file JSON. Infine l'algoritmo ritornerà la direzione o la corsia dove si trova l'oggetto.
