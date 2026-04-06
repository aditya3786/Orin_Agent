#!/usr/bin/env python3
"""Script to add test documents to the vector store."""

import os
import sys

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from app.rag import document_manager

DOCUMENTS = [
    {
        "file_path": "test_docs/leave_policy.txt",
        "department": "HR",
        "document_type": "policy",
        "metadata": {"title": "Leave Policy", "author": "HR Department"},
    },
    {
        "file_path": "test_docs/it_support_policy.txt",
        "department": "IT",
        "document_type": "policy",
        "metadata": {"title": "IT Support & Equipment Policy", "author": "IT Department"},
    },
    {
        "file_path": "test_docs/expense_reimbursement_policy.txt",
        "department": "Finance",
        "document_type": "policy",
        "metadata": {"title": "Expense Reimbursement Policy", "author": "Finance Department"},
    },
    {
        "file_path": "test_docs/employee_onboarding_guide.txt",
        "department": "HR",
        "document_type": "guide",
        "metadata": {"title": "Employee Onboarding Guide", "author": "HR Department"},
    },
]

def add_test_documents():
    """Add all test documents to the vector store."""
    success_count = 0
    for doc in DOCUMENTS:
        try:
            doc_ids = document_manager.add_official_document(
                file_path=doc["file_path"],
                department=doc["department"],
                document_type=doc["document_type"],
                additional_metadata=doc["metadata"],
            )
            print(f"✅ Indexed '{doc['file_path']}' → {len(doc_ids)} chunk(s)")
            success_count += 1
        except Exception as e:
            print(f"❌ Failed '{doc['file_path']}': {e}")

    print(f"\n{success_count}/{len(DOCUMENTS)} documents indexed successfully.")

if __name__ == "__main__":
    add_test_documents()