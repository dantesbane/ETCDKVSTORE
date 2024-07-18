from unittest.mock import patch, MagicMock
import unittest
from io import StringIO
from script import list_all_keys, get_key_and_print_value, get_key_and_value_and_put, delete_key

class TestEtcdScript(unittest.TestCase):

    @patch('script.etcd3.client')
    def test_list_all_keys(self, mock_etcd_client):
        # Setup the mock to return an iterator of tuples when get_all is called
        mock_etcd_client.return_value.get_all.return_value = iter([
            (b'key1', MagicMock(key=b'key1')),
            (b'key2', MagicMock(key=b'key2'))
        ])
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            list_all_keys(mock_etcd_client())
            self.assertIn("List of Keys:\nkey1\nkey2", mock_stdout.getvalue().strip())

    @patch('script.etcd3.client')
    def test_get_key_and_print_value_existing(self, mock_etcd_client):
        mock_etcd_client.return_value.get.return_value = (b'value', MagicMock())
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout, patch('sys.stdin', StringIO("existing_key\n")):
            get_key_and_print_value(mock_etcd_client())
            self.assertIn("The value is: value", mock_stdout.getvalue().strip())

    @patch('script.etcd3.client')
    def test_get_key_and_print_value_non_existing(self, mock_etcd_client):
        mock_etcd_client.return_value.get.return_value = (None, None)
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout, patch('sys.stdin', StringIO("non_existing_key\n")):
            get_key_and_print_value(mock_etcd_client())
            self.assertIn("Key does not exist!", mock_stdout.getvalue().strip())

    @patch('script.etcd3.client')
    def test_get_key_and_value_and_put(self, mock_etcd_client):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout, patch('sys.stdin', StringIO("new_key\nnew_value\n")):
            get_key_and_value_and_put(mock_etcd_client())
            self.assertIn("Key-value pair added successfully.", mock_stdout.getvalue().strip())

    @patch('script.etcd3.client')
    def test_delete_key_existing(self, mock_etcd_client):
        mock_etcd_client.return_value.delete.return_value = True
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout, patch('sys.stdin', StringIO("key_to_delete\n")):
            delete_key(mock_etcd_client())
            self.assertIn("Key deleted successfully!", mock_stdout.getvalue().strip())

    @patch('script.etcd3.client')
    def test_delete_key_non_existing(self, mock_etcd_client):
        mock_etcd_client.return_value.delete.return_value = False
        
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout, patch('sys.stdin', StringIO("non_existing_key\n")):
            delete_key(mock_etcd_client())
            self.assertIn("Key not found!", mock_stdout.getvalue().strip())

if __name__ == '__main__':
    unittest.main()

