def solution_cost(solution, system_load):
    """
    Returns the cost of the given solution against container load

    :param solution: Solution to analyse
    :type solution: list

    :param system_load: System load
    :type system_load: int

    :returns: Cost of the given solution
    :rtype: int
    """
    return [abs(system_load - sum(solution)), len(solution)]


def solutions(container_types, system_load, containers=[]):
    """
    Returns a generator to iterate a list of possible solutions

    :param container_types: List of container types
    :type container_types: list

    :param system_load: System load
    :type system_load: int

    :param containers: Solution so far
    :type containers: list

    :returns: A generator to iterate a list of possible solutions
    :rtype: generator
    """
    container_load = sum(containers)
    if container_load == system_load:
        yield containers
    elif container_load > system_load:
        yield containers
    elif not len(container_types):
        # Ignore, there is no solution available
        pass
    else:
        # Check multiple occurrences of the same container type
        yield from solutions(
            container_types[:],
            system_load,
            containers=containers + [container_types[0]]
        )

        # Check other container types
        yield from solutions(
            container_types[1:],
            system_load,
            containers=containers
        )


def solve(container_types, system_load):
    """
    Returns the best solution for the given system load and container types

    :param container_types: List of container types
    :type container_types: list

    :param system_load: System load
    :type system_load: int

    :returns: The the most cost effective solution
    :rtype: list
    """
    container_types = list(set(container_types))
    return min(solutions(container_types, system_load),
               key=lambda s: solution_cost(s, system_load))
