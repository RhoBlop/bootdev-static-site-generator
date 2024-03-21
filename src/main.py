from htmlnode import ParentNode, LeafNode

def main():
    print(ParentNode(
        tag="p",
        children=[
            LeafNode(tag="b", content="Bold text"),
            LeafNode(content="Normal text"),
            LeafNode(tag="i", content="Italic text"),
            LeafNode(content="Normal text"),
        ],
    ).to_html())

if __name__ == "__main__":
    main()