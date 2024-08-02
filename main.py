from database import init_db
from operations import add_product, add_component, add_to_product_structure, get_product, get_component, get_product_structure, view_product_structure_tree6

def main():
    init_db()

    while True:
        print("\n1. Add Product")
        print("2. Add Component")
        print("3. Add to Product Structure")
        print("4. View Product")
        print("5. View Component")
        print("6. View Product Structure")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            description = input("Enter product description: ")
            product_id = add_product(name, description)
            print(f"Product added with ID: {product_id}")

        elif choice == '2':
            name = input("Enter component name: ")
            quantity = float(input("Enter quantity: "))
            unit = input("Enter unit of measure: ")
            component_id = add_component(name, quantity, unit)
            print(f"Component added with ID: {component_id}")

        elif choice == '3':
            parent_id = int(input("Enter parent product ID: "))
            child_id = int(input("Enter child ID: "))
            child_type = input("Enter child type (product/component): ")
            quantity = float(input("Enter quantity: "))
            structure_id = add_to_product_structure(parent_id, child_id, child_type, quantity)
            print(f"Structure added with ID: {structure_id}")

        elif choice == '4':
            product_id = int(input("Enter product ID: "))
            product = get_product(product_id)
            if product:
                print(f"Product: {product.name}, Description: {product.description}")
            else:
                print("Product not found")

        elif choice == '5':
            component_id = int(input("Enter component ID: "))
            component = get_component(component_id)
            if component:
                print(f"Component: {component.name}, Quantity: {component.quantity}, Unit: {component.unit_of_measure}")
            else:
                print("Component not found")

        elif choice == '6':
            product_id = int(input("Enter product ID: "))
            try:
                success, result = view_product_structure_tree(product_id)
                if success:
                    print(result)
                else:
                    print(result)  # This will print "Product not found."
            except Exception as e:
                print(f"An error occurred: {str(e)}")

        elif choice == '7':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()