from concurrent.futures import ThreadPoolExecutor


def run_generation(llm):
    return llm.generate(
        "hello",
    )


def test_llm_concurrent_generation(
    dummy_llm,
):
    """
    Stress test dummy LLM concurrency.
    """

    total_requests = 100
    workers = 20

    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(
            executor.map(
                lambda _: run_generation(dummy_llm),
                range(total_requests),
            )
        )

    assert len(results) == total_requests
