def solution(new_id):
    new_id = new_id.lower()

    for c in new_id:
        if c.isnumeric() or c.islower() or c in ['-', '_', '.']:
            continue
        new_id = new_id.replace(c, '')

    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    new_id = new_id.strip('.')

    if not new_id:
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15].strip('.')

    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id
