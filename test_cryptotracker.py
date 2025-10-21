# test_cryptotracker.py
"""
Tests for CryptoTracker module.
"""

import unittest
from cryptotracker import CryptoTracker

class TestCryptoTracker(unittest.TestCase):
    """Test cases for CryptoTracker class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoTracker()
        self.assertIsInstance(instance, CryptoTracker)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoTracker()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
