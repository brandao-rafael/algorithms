def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    student_counter = 0
    if not target_time or target_time is None:
        return None
    for entry, end in permanence_period:
        if (
            entry is None
            or end is None
            or isinstance(entry, str)
            or isinstance(end, str)
        ):
            return None
        if (target_time > int(entry) and target_time < int(end)) or (
            target_time == int(entry) or target_time == int(end)
        ):
            student_counter += 1
    return student_counter
