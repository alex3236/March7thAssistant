def run_cloud_tasks():
    """Worker function that runs the main automation tasks inside a cloud game session.

    Designed to be used as a multiprocessing.Process target so the parent process
    can enforce a wall-clock timeout and terminate this worker if it runs too long.
    All modules are imported inside the function to keep the module importable with
    no side-effects (required for the 'spawn' start method on Windows).
    """
    from tasks.daily.daily import Daily
    import tasks.reward as reward

    reward.start_specific("dispatch")
    Daily.start()
    reward.start()
