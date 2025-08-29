def format_cents(cents: int) -> str:
    sign = "[+]" if cents > 0 else "[-]"
    converted = abs(cents) / 100

    return f"{sign} R$ {'{:,.2f}'.format(converted).replace(',', 'X').replace('.', ',').replace('X', '.')}"