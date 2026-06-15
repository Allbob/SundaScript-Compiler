import unittest
from src.lexer import Lexer
from src.parser import Parser

class TestFullCoverage(unittest.TestCase):
    def test_all_features(self):
        source = '''
        # Test class & inheritance
        kelas Kucing (Hewan) {
            jieun meong(sorangan) {
                citak("Meong")
            }
        }

        # Test Try Except
        coba {
            angkat Error()
        } iwal Error salaku e {
            citak(e)
        } tungtungna {
            liwatan
        }

        # Test Import
        candak os
        ti math candak pi

        # Test Async
        babarengan jieun proses() {
            antosan sleep(1)
        }

        # Test Match Case
        cocog x {
            kaayaan 1 {
                citak("Satu")
            }
            kaayaan 2 {
                eureun
            }
        }

        # Test Context Manager
        sareng_ieu buka("file.txt") salaku f {
            baca(f)
        }

        # Builtins coverage check
        panjang(daptar())
        himpunan()
        mutlak(-5)
        '''
        lexer = Lexer(source)
        tokens = lexer.tokenize()
        
        parser = Parser(tokens)
        cst = parser.parse_program()
        
        from src.ast_builder import ASTBuilder
        builder = ASTBuilder()
        ast = builder.build(cst)
        
        print("\n--- TEST FULL COVERAGE PASSED (LEXER & PARSER) ---")
        print("\n==================== FASE 4: ABSTRACT SYNTAX TREE (FULL COVERAGE) ====================")
        print(ast.print_ast())
        
        # Verify CST nodes
        nodes = cst.children
        self.assertEqual(nodes[0].name, "class_def_stmt")
        self.assertEqual(nodes[1].name, "try_stmt")
        self.assertEqual(nodes[2].name, "import_stmt")
        self.assertEqual(nodes[3].name, "from_import_stmt")
        self.assertEqual(nodes[4].name, "async_stmt")
        self.assertEqual(nodes[5].name, "match_stmt")
        self.assertEqual(nodes[6].name, "with_stmt")
        self.assertEqual(nodes[7].name, "function_call_stmt") # panjang(...)

if __name__ == '__main__':
    unittest.main()
