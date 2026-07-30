def build_prompt(proposal_string: str, context: str, risk_floor: str) -> str:
    return f"""You are assisting a UK Higher Education ethics committee with a PRELIMINARY review of a research proposal.

RETRIEVED POLICY CONTEXT:
{context}

RESEARCH PROPOSAL:
{proposal_string}

MANDATORY CONSTRAINT:
You MUST assign a risk level of {risk_floor} or higher. Do not assign a lower risk level than this floor under any circumstances, even if your own analysis suggests a lower risk.

Produce a structured assessment with exactly these sections:

RISK LEVEL
[state LOW, MEDIUM, or HIGH]

SECTION-BY-SECTION ASSESSMENT
[assess each part of the proposal against the retrieved policy context]

FLAGGED CONCERNS
[list specific ethical concerns, citing which policy document each concern relates to]

POLICY DOCUMENTS RETRIEVED
[list the source documents used in the retrieved context]

REVIEWER NOTICE
This is a preliminary, AI-assisted assessment. It does not constitute institutional ethics approval and must be reviewed by a qualified human ethics reviewer before any decision is made.
"""
