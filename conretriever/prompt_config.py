task_to_query_type = {
    'eli5': 'a user question',
    'hotpot_qa': 'a multi-hop question',
    'fever': 'a claim',
    'msmarco_passage': 'a web search query',
    'msmarco_document': 'a web search query',
    'nq': 'a question',
    'squad': 'a question',
    'triviaqa': 'a question',
    'quora_duplicate': 'a question',
    'agnews': 'a news title',
    'amazon_qa': 'a user question',
    'amazon_review': 'a title',
    'ccnews_title_text': 'a news title',
    'gooaq_pairs': 'a user question',
    'medmcqa': 'a medical question',
    'npr': 'a news title',
    'paq_pairs': 'a question',
    's2orc_title_abstract': 'a paper title',
    'simple_wiki': 'a Wikipedia sentence',
    'wikihow': 'a Wikipedia summary',
    'xsum': 'a news summary',
    'yahoo_answers_title_answer': 'a question',
    'zero_shot_re': 'a Wikipedia question',
    'fiqa': 'a financial question',
}

task_to_passage_type = {
    'eli5': 'answers',
    'hotpot_qa': 'supporting documents',
    'fever': 'documents that support or refute the claim',
    'msmarco_passage': 'relevant passages that answer the query',
    'msmarco_document': 'relevant documents that answer the query',
    'nq': 'Wikipedia passages that answer the question',
    'squad': 'Wikipedia passages that answer the question',
    'triviaqa': 'Wikipedia passages that answer the question',
    'quora_duplicate': 'questions that have the same meaning as the question',
    'agnews': 'news articles that support the news title',
    'amazon_qa': 'reviews that answer the question',
    'amazon_review': 'reviews relevant to the title',
    'ccnews_title_text': 'news articles that support the news title',
    'gooaq_pairs': 'answers',
    'medmcqa': 'answers',
    'npr': 'news articles that support the news title',
    'paq_pairs': 'documents that answer the question',
    's2orc_title_abstract': 'paper abstract relevant to the paper title',
    'simple_wiki': 'simplified Wikipedia sentences aligning to the given Wikipedia sentence',
    'wikihow': 'Wikipedia passages that enrich the Wikipedia summary',
    'xsum': 'news articles that enrich the news summary',
    'yahoo_answers_title_answer': 'answers',
    'zero_shot_re': 'Wikipedia sentences that answer the Wikipedia question',
    'fiqa': 'user replies that best answer the question',
}
