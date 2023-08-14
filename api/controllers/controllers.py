from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from models import models

from uuid import uuid4
import re


# --------------------------------------------------


def get_user(id, db: Session):
    """Get a user by ID.

    Args:
        id: The ID of the user to get.
        db: The database session.

    Returns:
        The user, or None if not found.

    Raises:
        HTTPException: If the user is not found.
    """

    try:
        user = db.query(models.User).filter(models.User.id == id).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)

    return user


def add_user(user, db: Session):
    """Add a new user.

    Args:
        user: The user to add.
        db: The database session.

    Returns:
        The newly created user.

    Raises:
        HTTPException: If the user already exists.
    """

    user = user.dict()
    try:
        new_user = models.User(
            id = str(uuid4()),
            first_name = user["first_name"],
            last_name = user["last_name"],
            email = user["email"],
            password = user["password"], #Hash.hash_password(user["password"]),
        )
        addresses = []
        for address in user["addresses"]:
            new_address = models.Address(
                user_id = new_user.id,
                address_1 = address["address_1"],
                address_2 = address.get("address_2"),
                city = address["city"],
                state = address["state"],
                zip = address["zip"],
                country = address["country"],
            )
            addresses.append(new_address)

        db.add(new_user)
        db.add_all(addresses)
        db.commit()
        db.refresh(new_user)

    except Exception as e:
        if re.search(r'duplicate key value violates unique constraint', e.args[0]) is not None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return new_user


def update_user(id, user, db: Session):
    """Update a user.

    Args:
        id: The ID of the user to update.
        user: The updated user data.
        db: The database session.

    Returns:
        The updated user.

    Raises:
        HTTPException: If the user is not found.
    """

    try:
        user_in_db = db.query(models.User).filter(models.User.id == id).first()
        if user_in_db is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        user_in_db.first_name = user.first_name
        user_in_db.last_name = user.last_name
        user_in_db.email = user.email
        user_in_db.password = user.password
        db.commit()

    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)


def delete_user(id, db: Session):
    try:
        db.query(models.User).where(models.User.id == id).delete()
        db.commit()

    except Exception as e:
        if re.search(r'violates foreign key constraint', e.args[0]) is not None: 
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail='Violates foreign key constraint. You have to delete the address related to this user to proceed')
        else: 
            raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)


# --------------------------------------------------


def get_address(user_id, db: Session):
    """Get all addresses for a user.

    Args:
        user_id: The ID of the user.
        db: The database session.

    Returns:
        A list of addresses.

    Raises:
        HTTPException: If the user is not found.
    """

    try:
        address = db.query(models.Address).filter(models.Address.user_id == user_id).all()
        if address is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)

    return address


def add_address(address, db: Session):
    """Add a new address.

    Args:
        address: The address to add.
        db: The database session.

    Returns:
        The newly created address.

    Raises:
        HTTPException: If the address already exists.
    """

    address = address.dict()
    try:
        new_address = models.Address(
            user_id = address["user_id"],
            address_1 = address["address_1"],
            address_2 = address["address_2"],
            city = address["city"],
            state = address["state"],
            zip = address["zip"],
            country = address["country"],
        )
        db.add(new_address)
        db.commit()
        db.refresh(new_address)

    except Exception as e:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT)


def update_address(id, address, db: Session):
    """Update an address.

    Args:
        id: The ID of the address to update.
        address: The updated address data.
        db: The database session.

    Returns:
        The updated address.

    Raises:
        HTTPException: If the address is not found.
    """

    try:
        address_in_db = db.query(models.Address).filter(models.Address.id == id).first()
        if address_in_db is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        address_in_db.address_1 = address.address_1
        address_in_db.address_2 = address.address_2
        address_in_db.city = address.city
        address_in_db.state = address.state
        address_in_db.zip = address.zip
        address_in_db.country = address.country
        db.commit()

    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)


def delete_address(id, db: Session):
    """Delete an address.

    Args:
        id: The ID of the address to delete.
        db: The database session.

    Raises:
        HTTPException: If the address is not found.
    """

    try:
        db.query(models.Address).where(models.Address.id == id).delete()
        db.commit()

    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR)