import unittest
from textnode import TextNode, TextType
from blocknode import block_to_block_type, BlockType  # replace with your actual module name

class TestBlockToBlockType(unittest.TestCase):
    
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
        # Not a heading - no space after #
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.PARAGRAPH)
        # Not a heading - too many #
        self.assertEqual(block_to_block_type("####### Too many"), BlockType.PARAGRAPH)

    def test_code(self):
        self.assertEqual(block_to_block_type("```\ncode block\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("```\n```"), BlockType.CODE)
        # Not a code block - only starts with backticks
        self.assertEqual(block_to_block_type("```\nno ending"), BlockType.PARAGRAPH)
        # Not a code block - only ends with backticks
        self.assertEqual(block_to_block_type("no starting\n```"), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- item 1"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("- item 1\n- item 2\n- item 3"), BlockType.UNORDERED_LIST)
        # Not an unordered list - missing space after dash
        self.assertEqual(block_to_block_type("-no space"), BlockType.PARAGRAPH)
        # Not an unordered list - one line doesn't have dash
        self.assertEqual(block_to_block_type("- item 1\nno dash\n- item 3"), BlockType.PARAGRAPH)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. item 1"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("1. item 1\n2. item 2\n3. item 3"), BlockType.ORDERED_LIST)
        # Not an ordered list - numbers not sequential
        self.assertEqual(block_to_block_type("1. item 1\n3. item 3"), BlockType.PARAGRAPH)
        # Not an ordered list - doesn't start with 1
        self.assertEqual(block_to_block_type("2. item 2\n3. item 3"), BlockType.PARAGRAPH)
        # Not an ordered list - missing space after number
        self.assertEqual(block_to_block_type("1.no space"), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()