import re
from typing import List
from src.token import Token, TokenType

# Himpunan keyword dan fungsi bawaan yang dipetakan ti project_setup.md
KEYWORDS = {
    'Leres', 'Lepat', 'Suwung', # Boolean / Nilai Khusus yang masuk ke keyword
    'jeung', 'atawa', 'henteu', 'lamun', 'lamun_sanes', 'sanesna', 'pikeun', 'salami', 
    'dina', 'eureun', 'teras', 'liwatan', 'jieun', 'pulangkeun', 'hasilkeun', 
    'fungsi_leutik', 'kelas', 'sorangan', 'indung', 'coba', 'iwal', 'tungtungna', 
    'angkat', 'pastikeun', 'candak', 'ti', 'salaku', 'sareng_ieu', 'babarengan', 
    'antosan', 'cocog', 'kaayaan', 'sadayana', 'sanes_lokal', 'hapus', 'nyaeta'
}

BUILTINS = {
    'citak', 'tanya', 'angka', 'desimal', 'tulisan', 'logika', 'kompleks',
    'daptar', 'kumpulan', 'himpunan', 'kamus', 'himpunan_baku', 'mutlak',
    'buleudkeun', 'pangkat', 'bagisesa', 'jumlah', 'pangluhurna', 'panghandapna',
    'panjang', 'rentang', 'daptarkeun', 'gabung', 'ulang', 'lajeng',
    'balikeun', 'urutkeun', 'sadayanana', 'salah_sahiji', 'jenis', 'uji_kelas',
    'uji_subkelas', 'tanda', 'tiasa_panggil', 'aksara', 'urutan', 'aski', 'biner',
    'oktal', 'heksa', 'candak_sipat', 'atur_sipat', 'aya_sipat',
    'hapus_sipat', 'sadayanana_global', 'lokalna', 'variabelna', 'arah',
    'evaluasi', 'jalankeun', 'kompilasi', 'buka', 'bait', 'susunan_bait',
    'tempo_memori', 'petakeun', 'saring', 'properti', 'metode_statis',
    'metode_kelas', '__candak__', 'titik_eureun', 'bentuk',
    'wakil', 'acak', 'tolong', 'potong', 'objek'
}

class LexerError(Exception):
    def __init__(self, message: str, line: int, column: int):
        super().__init__(f"LexerError at line {line}, col {column}: {message}")

class Lexer:
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.pos = 0
        self.line = 1
        self.column = 1
        
        # Spesifikasi Regex (berurutan, rule terpanjang didahulukan)
        self.rules = [
            ('SKIP', r'[ \t]+'),
            ('COMMENT', r'#.*'),
            ('NEWLINE', r'\n'),
            ('STRING', r'"[^"]*"|\'[^\']*\''),
            ('NUMBER', r'\d+\.\d+|\d+'),
            ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('OPERATOR', r'==|!=|<=|>=|<|>|\+|-|\*|/|='),
            ('LBRACE', r'\{'),
            ('RBRACE', r'\}'),
            ('LPAREN', r'\('),
            ('RPAREN', r'\)'),
            ('COMMA', r','),
            ('MISMATCH', r'.')
        ]
        
        self.regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.rules)
        self.scanner = re.compile(self.regex)

    def tokenize(self) -> List[Token]:
        tokens = []
        for match in self.scanner.finditer(self.source_code):
            kind = match.lastgroup
            value = match.group()
            
            if kind == 'SKIP' or kind == 'COMMENT':
                self.column += len(value)
                continue
            elif kind == 'NEWLINE':
                self.line += 1
                self.column = 1
                continue
            elif kind == 'MISMATCH':
                raise LexerError(f"Karakter Ilegal '{value}'", self.line, self.column)
            
            token_type = self._determine_token_type(kind, value)
            tokens.append(Token(token_type, value, self.line, self.column))
            self.column += len(value)
            
        tokens.append(Token(TokenType.EOF, "", self.line, self.column))
        return tokens
        
    def _determine_token_type(self, kind: str, value: str) -> TokenType:
        if kind == 'ID':
            if value in KEYWORDS:
                return TokenType.KEYWORD
            elif value in BUILTINS:
                return TokenType.BUILTIN
            else:
                return TokenType.IDENTIFIER
                
        mapping = {
            'STRING': TokenType.STRING,
            'NUMBER': TokenType.NUMBER,
            'OPERATOR': TokenType.OPERATOR,
            'LBRACE': TokenType.LBRACE,
            'RBRACE': TokenType.RBRACE,
            'LPAREN': TokenType.LPAREN,
            'RPAREN': TokenType.RPAREN,
            'COMMA': TokenType.COMMA
        }
        return mapping[kind]
