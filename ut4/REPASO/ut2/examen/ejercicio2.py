def semaforo(signal: str)-> str:
    match signal:
        case "🟢":
            return "🟠"
        case "🟠":
            return "🔴"
        case "🔴":
            return "🟢"
        case _:
            return None

