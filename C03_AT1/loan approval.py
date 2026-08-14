# ==========================================================
# INTELLIGENT LOAN APPROVAL SYSTEM
# Knowledge Representation and Reasoning
# ==========================================================

# ----------------------------------------------------------
# 1. KNOWLEDGE BASE - FACTS
# ----------------------------------------------------------

facts = {
    # Arun's facts
    "StableEmployment(Arun)",
    "SufficientIncome(Arun)",
    "HighCreditScore(Arun)",
    "GoodRepayment(Arun)",
    "ExistingLoan(Arun)",
    "NotExcessiveDebt(Arun)",

    # Bala's facts
    "StableEmployment(Bala)",
    "SufficientIncome(Bala)",
    "HighCreditScore(Bala)",
    "GoodRepayment(Bala)",

    # Chitra's facts
    "StableEmployment(Chitra)",
    "SufficientIncome(Chitra)",
    "LowCreditScore(Chitra)",
    "BadRepayment(Chitra)",
    "ExcessiveDebt(Chitra)"
}


# ----------------------------------------------------------
# 2. KNOWLEDGE BASE - RULES
# ----------------------------------------------------------

rules = [
    # R1
    (
        ["StableEmployment(x)", "SufficientIncome(x)"],
        "PreliminaryApproval(x)"
    ),

    # R2
    (
        ["HighCreditScore(x)", "GoodRepayment(x)"],
        "LowRisk(x)"
    ),

    # R3
    (
        ["PreliminaryApproval(x)", "LowRisk(x)"],
        "LoanEligible(x)"
    ),

    # R4
    (
        ["LoanEligible(x)", "NotExcessiveDebt(x)"],
        "LoanApproved(x)"
    ),

    # R5
    (
        ["LowCreditScore(x)"],
        "HighRisk(x)"
    ),

    # R6
    (
        ["BadRepayment(x)"],
        "HighRisk(x)"
    ),

    # R7
    (
        ["ExcessiveDebt(x)"],
        "HighRisk(x)"
    ),

    # R8
    (
        ["SufficientIncome(x)", "HighCreditScore(x)"],
        "FinanciallyStrong(x)"
    ),

    # R9
    (
        ["StableEmployment(x)",
         "GoodRepayment(x)",
         "HighCreditScore(x)"],
        "ReliableCustomer(x)"
    ),

    # R10
    (
        ["ReliableCustomer(x)", "FinanciallyStrong(x)"],
        "LoanRecommendation(x)"
    )
]


# ----------------------------------------------------------
# 3. UNIFICATION AND SUBSTITUTION
# ----------------------------------------------------------

def unify(pattern, fact):
    """
    Simple unification:
    Example:
    StableEmployment(x)
    StableEmployment(Arun)

    MGU = {x: Arun}
    """

    if "(" not in pattern or "(" not in fact:
        return None

    predicate1 = pattern.split("(")[0]
    predicate2 = fact.split("(")[0]

    if predicate1 != predicate2:
        return None

    argument1 = pattern.split("(")[1].replace(")", "")
    argument2 = fact.split("(")[1].replace(")", "")

    if argument1 == "x":
        return {"x": argument2}

    if argument1 == argument2:
        return {}

    return None


# ----------------------------------------------------------
# 4. APPLY SUBSTITUTION
# ----------------------------------------------------------

def substitute(expression, substitution):
    for variable, value in substitution.items():
        expression = expression.replace(variable, value)

    return expression


# ----------------------------------------------------------
# 5. FORWARD CHAINING
# ----------------------------------------------------------

def forward_chaining(initial_facts, customer):

    derived_facts = set(initial_facts)

    print("\n========== FORWARD CHAINING ==========")

    changed = True

    while changed:
        changed = False

        for conditions, conclusion in rules:

            # Replace x with customer
            required = [
                condition.replace("(x)", f"({customer})")
                for condition in conditions
            ]

            result = conclusion.replace("(x)", f"({customer})")

            # Check whether all conditions are satisfied
            if all(condition in derived_facts
                   for condition in required):

                if result not in derived_facts:

                    derived_facts.add(result)
                    changed = True

                    print("Rule Applied:", conditions,
                          "->", conclusion)
                    print("Derived:", result)

    return derived_facts


# ----------------------------------------------------------
# 6. BACKWARD CHAINING
# ----------------------------------------------------------

def backward_chaining(goal, facts, visited=None):

    if visited is None:
        visited = set()

    # Goal already known
    if goal in facts:
        print("Fact found:", goal)
        return True

    # Avoid infinite loops
    if goal in visited:
        return False

    visited.add(goal)

    print("Trying to prove:", goal)

    # Search for a rule whose conclusion matches goal
    for conditions, conclusion in rules:

        # Convert x into actual customer name
        customer = goal.split("(")[1].replace(")", "")

        actual_conclusion = conclusion.replace("(x)", f"({customer})")

        if actual_conclusion == goal:

            print("Using Rule:", conditions,
                  "->", conclusion)

            all_true = True

            for condition in conditions:

                actual_condition = condition.replace(
                    "(x)", f"({customer})"
                )

                if not backward_chaining(
                        actual_condition,
                        facts,
                        visited):

                    all_true = False
                    break

            if all_true:
                return True

    return False


# ----------------------------------------------------------
# 7. RESOLUTION DEMONSTRATION
# ----------------------------------------------------------

def resolution_demo():

    print("\n========== RESOLUTION ==========")

    print("\nGoal:")
    print("LoanApproved(Arun)")

    print("\nAssume the opposite:")
    print("NOT LoanApproved(Arun)")

    print("\nRelevant Rule R4:")
    print("LoanEligible(x) AND NotExcessiveDebt(x)")
    print("-> LoanApproved(x)")

    print("\nClause form:")
    print("NOT LoanEligible(x) OR ExcessiveDebt(x)")
    print("OR LoanApproved(x)")

    print("\nSubstitution:")
    print("{x / Arun}")

    print("\nAfter substitution:")
    print("NOT LoanEligible(Arun)")
    print("OR ExcessiveDebt(Arun)")
    print("OR LoanApproved(Arun)")

    print("\nGiven:")
    print("NOT LoanApproved(Arun)")

    print("\nResolution gives:")
    print("NOT LoanEligible(Arun)")
    print("OR ExcessiveDebt(Arun)")

    print("\nGiven:")
    print("NotExcessiveDebt(Arun)")

    print("\nTherefore:")
    print("NOT LoanEligible(Arun)")

    print("\nBut forward reasoning proves:")
    print("LoanEligible(Arun)")

    print("\nContradiction obtained!")

    print("\nTherefore:")
    print("LoanApproved(Arun) is TRUE")


# ----------------------------------------------------------
# 8. MAIN PROGRAM
# ----------------------------------------------------------

print("===================================================")
print("       INTELLIGENT LOAN APPROVAL SYSTEM")
print("===================================================")

print("\nKnowledge Base contains:",
      len(facts), "initial facts")

print("\nInitial Facts:")
for fact in sorted(facts):
    print(" -", fact)


# ----------------------------------------------------------
# UNIFICATION EXAMPLE
# ----------------------------------------------------------

print("\n========== UNIFICATION ==========")

pattern = "StableEmployment(x)"
fact = "StableEmployment(Arun)"

substitution = unify(pattern, fact)

print("Expression 1:", pattern)
print("Expression 2:", fact)

if substitution is not None:
    print("Unification Successful")
    print("MGU =", substitution)

    result = substitute(pattern, substitution)

    print("After Substitution:", result)

else:
    print("Unification Failed")


# ----------------------------------------------------------
# FORWARD CHAINING FOR ARUN
# ----------------------------------------------------------

derived = forward_chaining(facts, "Arun")


print("\n========== DERIVED KNOWLEDGE FOR ARUN ==========")

for fact in sorted(derived):

    if "(Arun)" in fact:
        print(" -", fact)


# ----------------------------------------------------------
# FINAL FORWARD-CHAINING RESULT
# ----------------------------------------------------------

print("\n========== FINAL DECISION ==========")

if "LoanApproved(Arun)" in derived:
    print("Arun is RECOMMENDED for loan approval.")
else:
    print("Arun is NOT recommended for loan approval.")


# ----------------------------------------------------------
# BACKWARD CHAINING
# ----------------------------------------------------------

print("\n========== BACKWARD CHAINING ==========")

query = "LoanApproved(Arun)"

if backward_chaining(query, derived):
    print("\nBackward Chaining Result:")
    print("LoanApproved(Arun) = TRUE")
else:
    print("\nBackward Chaining Result:")
    print("LoanApproved(Arun) = FALSE")


# ----------------------------------------------------------
# RESOLUTION
# ----------------------------------------------------------

resolution_demo()


# ----------------------------------------------------------
# FINAL SUMMARY
# ----------------------------------------------------------

print("\n===================================================")
print("                  FINAL RESULT")
print("===================================================")

print("Customer                : Arun")
print("Stable Employment       : YES")
print("Sufficient Income       : YES")
print("High Credit Score       : YES")
print("Good Repayment History  : YES")
print("Excessive Debt          : NO")
print("Preliminary Approval    : YES")
print("Low Risk                : YES")
print("Loan Eligible           : YES")
print("Loan Approved           : YES")
print("===================================================")
