from database import get_session
from models import Product, Component, ProductStructure
from sqlalchemy.orm import joinedload
from anytree import Node, RenderTree
#print("Importing operations module")

def add_product(name, description):
    session = get_session()
    new_product = Product(name=name, description=description)
    session.add(new_product)
    session.commit()
    product_id = new_product.id
    session.close()
    return product_id

def add_component(name, quantity, unit_of_measure):
    session = get_session()
    new_component = Component(name=name, quantity=quantity, unit_of_measure=unit_of_measure)
    session.add(new_component)
    session.commit()
    component_id = new_component.id
    session.close()
    return component_id

def add_to_product_structure(parent_product_id, child_id, child_type, quantity):
    session = get_session()
    new_structure = ProductStructure(
        parent_product_id=parent_product_id,
        child_id=child_id,
        child_type=child_type,
        quantity=quantity
    )
    session.add(new_structure)
    session.commit()
    structure_id = new_structure.id
    session.close()
    return structure_id

def get_product(product_id):
    session = get_session()
    product = session.query(Product).get(product_id)
    session.close()
    return product

def get_component(component_id):
    session = get_session()
    component = session.query(Component).get(component_id)
    session.close()
    return component

def get_product_structure(product_id):
    session = get_session()
    structure = session.query(ProductStructure).filter_by(parent_product_id=product_id).all()
    session.close()
    return structure

def build_product_tree(product_id, parent=None):
    session = get_session()
    product = session.query(Product).get(product_id)
    
    if not product:
        session.close()
        return None

    node = Node(f"{product.name} (Product)", parent=parent)
    
    structure_items = session.query(ProductStructure).filter_by(parent_product_id=product_id).all()
    
    for item in structure_items:
        if item.child_type == 'product':
            build_product_tree(item.child_id, parent=node)
        else:  # component
            component = session.query(Component).get(item.child_id)
            if component:
                Node(f"{component.name} (Component) - Qty: {item.quantity} {component.unit_of_measure}", parent=node)
    
    session.close()
    return node

def view_product_structure_tree(product_id):
    session = get_session()
    product = session.query(Product).get(product_id)
    session.close()

    if not product:
        return False, "Product not found."

    root = build_product_tree(product_id)
    if root:
        tree_representation = ""
        for pre, _, node in RenderTree(root):
            tree_representation += f"{pre}{node.name}\n"
        return True, tree_representation
    else:
        return True, "Product exists but has no structure."
# Add more operations as needed (update, delete, etc.)