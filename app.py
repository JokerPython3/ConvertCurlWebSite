

import sys
import json

def tokenize(curl_cmd: str) -> list[str]:
    tokens: list[str] = []
    current = ''
    in_quotes = False
    quote_char = ''
    for ch in curl_cmd:
        if ch in ('"', "'"):
            if not in_quotes:
                in_quotes = True
                quote_char = ch
            elif quote_char == ch:
                in_quotes = False
            else:
                current += ch
        elif ch == ' ' and not in_quotes:
            if current:
                tokens.append(current)
                current = ''
        else:
            current += ch
    if current:
        tokens.append(current)
    return tokens

def parse_curl(tokens: list[str]) -> tuple[str, str, dict, str | None]:
    method = 'get'
    url = ''
    headers: dict[str, str] = {}
    data = None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in ('-X', '--request'):
            i += 1
            if i < len(tokens):
                method = tokens[i].lower()
        elif token in ('-H', '--header'):
            i += 1
            if i < len(tokens) and ':' in tokens[i]:
                k, v = tokens[i].split(':', 1)
                headers[k.strip()] = v.strip()
        elif token in ('-d', '--data', '--data-raw', '--data-binary'):
            i += 1
            if i < len(tokens):
                data = tokens[i]
        elif token.startswith('http'):
            url = tokens[i]
        i += 1
    return method, url, headers, data

def generate_code(method: str, url: str, headers: dict[str, str], data: str | None) -> str:
    lines: list[str] = [
        'import requests',
        '',
        'session = requests.Session()',
        f'url = {repr(url)}',
        '',
    ]

    cookies_str = headers.pop('Cookie', None)
    if cookies_str:
        cookie_pairs = {}
        for cookie in cookies_str.split(';'):
            if '=' in cookie:
                k, v = cookie.strip().split('=', 1)
                cookie_pairs[k] = v
        lines.append(f'session.cookies.update({json.dumps(cookie_pairs, indent=4, ensure_ascii=False)})')
        lines.append('')

    if headers:
        lines.append(f'headers = {json.dumps(headers, indent=4, ensure_ascii=False)}')
    else:
        lines.append('headers = {}')


    body_arg = ''
    if data is not None:
        try:
            parsed_json = json.loads(data)
            lines.append(f'json_data = {json.dumps(parsed_json, indent=4, ensure_ascii=False)}')
            body_arg = 'json=json_data'
        except json.JSONDecodeError:
            if '&' in data and '=' in data:
                form_data = {}
                for pair in data.split('&'):
                    if '=' in pair:
                        k, v = pair.split('=', 1)
                        form_data[k] = v
                lines.append(f'data = {json.dumps(form_data, indent=4, ensure_ascii=False)}')
                body_arg = 'data=data'
            else:
                lines.append(f'data = {repr(data)}')
                body_arg = 'data=data'

    lines.append('')
    call = f'response = session.{method}(url, headers=headers'
    if body_arg:
        call += f', {body_arg}'
    call += ')'
    lines.append(call)
    lines.append('')
    lines.append('print(response.status_code)')
    lines.append('print(response.text)')
    return '\n'.join(lines)

def main():
    if len(sys.argv) != 2:
        print('Usage: python convert.py <input_file>')
        sys.exit(1)
    infile = sys.argv[1]
    try:
        with open(infile, 'r', encoding='utf-8') as f:
            curl_cmd = f.read().strip()
    except FileNotFoundError:
        print(f'Error: {infile} not found')
        sys.exit(1)

    tokens = tokenize(curl_cmd)
    method, url, headers, data = parse_curl(tokens)
    code = generate_code(method, url, headers, data)
    print(code)

if __name__ == '__main__':
    main()
