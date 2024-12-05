# parentheses.py

def complete_parentheses(expression):
    """
    Συμπληρώνει τις αριστερές παρενθέσεις σε μια αριθμητική παράσταση χωρίς αριστερές παρενθέσεις.

    Args:
        expression (list of str): Μια λίστα που αντιπροσωπεύει την αριθμητική παράσταση χωρίς αριστερές παρενθέσεις.

    Returns:
        list of str: Η αριθμητική παράσταση με σωστά τοποθετημένες αριστερές παρενθέσεις.
    """
    result = []  # Λίστα για την τελική παράσταση
    stack = []   # Στοίβα για την παρακολούθηση των τελεστών

    for token in expression:
        if token == ')':
            if stack:
                # Τοποθέτηση '(' πριν τον τελευταίο τελεστή
                pos = stack.pop()
                result.insert(pos, '(')
            else:
                # Τοποθέτηση '(' στην αρχή αν δεν υπάρχει τελεστής
                result.insert(0, '(')
            # Προσθήκη της ')'
            result.append(token)
        else:
            # Προσθήκη του token στο αποτέλεσμα
            result.append(token)
            # Αν είναι τελεστής, αποθήκευση της θέσης για πιθανή '('
            if token in ['+', '-', '*', '/']:
                stack.append(len(result))

    # Προσθήκη εναπομεινάντων '(' αν υπάρχουν
    while stack:
        pos = stack.pop()
        result.insert(pos, '(')

    return result


# Παραδείγματα χρήσης
if __name__ == '__main__':
    # Παράδειγμα 1
    expr1 = ['1', '+', '2', ')', '*', '3', '-', '4', ')', '*', '5', '-', '6', ')', ')', ')']
    completed_expr1 = complete_parentheses(expr1)
    print(''.join(completed_expr1))
    # Αναμενόμενο αποτέλεσμα: ((1+2)*((3-4)*(5-6)))

    # Παράδειγμα 2
    expr2 = ['4', '*', '5', ')', '/', '2', '+', '3', ')']
    completed_expr2 = complete_parentheses(expr2)
    print(''.join(completed_expr2))
    # Αναμενόμενο αποτέλεσμα: ((4*5)/(2+3))
