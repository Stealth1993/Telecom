import graphviz

def create_volte_call_flow():
    dot = graphviz.Digraph("VoLTE_Call_Flow", format="png")
    dot.attr(rankdir="LR")
    
    nodes = {
        "UE": "User Equipment",
        "eNB": "eNodeB",
        "MME": "Mobility Management Entity",
        "SGW": "Serving Gateway",
        "PGW": "PDN Gateway",
        "IMS": "IP Multimedia Subsystem"
    }
    for node, label in nodes.items():
        dot.node(node, label)
    
    dot.edge("UE", "eNB", label="Attach Request")
    dot.edge("eNB", "MME", label="Attach Request")
    dot.edge("MME", "SGW", label="Create Session")
    dot.edge("SGW", "PGW", label="Create Session")
    dot.edge("PGW", "IMS", label="SIP Register")
    
    dot.render("volte_call_flow", view=True)

def main():
    create_volte_call_flow()

if __name__ == "__main__":
    main()