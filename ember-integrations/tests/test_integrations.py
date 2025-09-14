from logic.integrations_engine import IntegrationsEngine

def run_tests():
    engine = IntegrationsEngine()
    engine.add_connection("Discord", {"status": "connected"})
    engine.add_connection("Notion", {"status": "pending"})

    print("Connections:", engine.list_connections())
    print("Discord:", engine.get_connection("Discord"))
    print("GitHub:", engine.get_connection("GitHub"))

if __name__ == "__main__":
    run_tests()
