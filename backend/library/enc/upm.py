from typing import List, Optional
from plumbum import local, CommandNotFound

class UnixPermissionManager:
    """
    A class to manage Unix users, groups, file permissions, and ACLs using the Plumbum library.
    """

    def __init__(self):
        self._local = local

    def add_user(self, username: str, group: Optional[str] = None) -> None:
        """
        Add a new user to the system.

        Args:
            username (str): The name of the user to add.
            group (Optional[str]): The primary group for the user (optional).

        Raises:
            CommandNotFound: If the required command is not found.
        """
        try:
            if group:
                self._local["useradd"]["-m", "-g", group, username]()
            else:
                self._local["useradd"]["-m", username]()
        except CommandNotFound as e:
            raise CommandNotFound(f"Command 'useradd' not found: {e}")

    def delete_user(self, username: str) -> None:
        """
        Delete a user from the system.

        Args:
            username (str): The name of the user to delete.

        Raises:
            CommandNotFound: If the required command is not found.
        """
        try:
            self._local["userdel"]["-r", username]()
        except CommandNotFound as e:
            raise CommandNotFound(f"Command 'userdel' not found: {e}")

    def add_group(self, groupname: str) -> None:
        """
        Add a new group to the system.

        Args:
            groupname (str): The name of the group to add.

        Raises:
            CommandNotFound: If the required command is not found.
        """
        try:
            self._local["groupadd"][groupname]()
        except CommandNotFound as e:
            raise CommandNotFound(f"Command 'groupadd' not found: {e}")

    def delete_group(self, groupname: str) -> None:
        """
        Delete a group from the system.

        Args:
            groupname (str): The name of the group to delete.

        Raises:
            CommandNotFound: If the required command is not found.
        """
        try:
            self._local["groupdel"][groupname]()
        except CommandNotFound as e:
            raise CommandNotFound(f"Command 'groupdel' not found: {e}")

    def set_file_permissions(self, filepath: str, mode: str) -> None:
        """
        Set file permissions using chmod.

        Args:
            filepath (str): The path to the file or directory.
            mode (str): The permission mode (e.g., "755").

        Raises:
            CommandNotFound: If the required command is not found.
        """
        try:
            self._local["chmod"][mode, filepath]()
        except CommandNotFound as e:
            raise CommandNotFound(f"Command 'chmod' not found: {e}")

    def set_file_owner(self, filepath: str, owner: str, group: Optional[str] = None) -> None:
        """
        Set the owner and/or group of a file or directory.

        Args:
            filepath (str): The path to the file or directory.
            owner (str): The new owner of the file.
            group (Optional[str]): The new group of the file (optional).

        Raises:
            CommandNotFound: If the required command is not found.
        """
        try:
            if group:
                self._local["chown"][f"{owner}:{group}", filepath]()
            else:
                self._local["chown"][owner, filepath]()
        except CommandNotFound as e:
            raise CommandNotFound(f"Command 'chown' not found: {e}")

    def set_acl(self, filepath: str, entity: str, permissions: str) -> None:
        """
        Set ACL permissions for a specific user or group.

        Args:
            filepath (str): The path to the file or directory.
            entity (str): The user or group (e.g., "u:john" or "g:developers").
            permissions (str): The ACL permissions (e.g., "rwx").

        Raises:
            CommandNotFound: If the required command is not found.
        """
        try:
            self._local["setfacl"]["-m", f"{entity}:{permissions}", filepath]()
        except CommandNotFound as e:
            raise CommandNotFound(f"Command 'setfacl' not found: {e}")

    def remove_acl(self, filepath: str, entity: str) -> None:
        """
        Remove ACL permissions for a specific user or group.

        Args:
            filepath (str): The path to the file or directory.
            entity (str): The user or group (e.g., "u:john" or "g:developers").

        Raises:
            CommandNotFound: If the required command is not found.
        """
        try:
            self._local["setfacl"]["-x", entity, filepath]()
        except CommandNotFound as e:
            raise CommandNotFound(f"Command 'setfacl' not found: {e}")

    def get_acl(self, filepath: str) -> List[str]:
        """
        Get the ACL permissions for a file or directory.

        Args:
            filepath (str): The path to the file or directory.

        Returns:
            List[str]: A list of ACL entries.

        Raises:
            CommandNotFound: If the required command is not found.
        """
        try:
            result = self._local["getfacl"][filepath]()
            return result.splitlines()
        except CommandNotFound as e:
            raise CommandNotFound(f"Command 'getfacl' not found: {e}")
        
