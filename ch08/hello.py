def handler(event, context):
    name = event.get("name", "world")
    return {"greeting": f"good day, {name}", "version": 2}
