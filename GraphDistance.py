

edges = [['A','B',5],['B','C',4],['C','D',8],['D','C',8],['D','E',6],['A','D',5],['C','E',2],['E','B',3],['A','E',7]]


class GraphDistance:

    def calculate_distance(self, logger):
        logger.info("Started calculating distance")
        route = ['A', 'D', 'C']
        logger.info(f"Calculating distance for route : {str(route)}")
        distance = 0
        route_step = 0
        from_node = route[route_step]
        to_node = route[route_step + 1]
        flag = True
        try:
            while flag:
                logger.info("Iteration through while loop")
                for edge in edges:
                    logger.info(f'Current node {str(edge)}')
                    logger.debug(f'Current iteration : {str(edge)} and Node : {from_node}')
                    if edge[0] is from_node:
                        if edge[1] is to_node:  # If next node matched we will increment our distance and node covered
                            distance += edge[2]
                            route_step += 1
                            from_node = route[route_step]
                            if route_step + 1 < len(route):
                                to_node = route[route_step + 1]
                            if from_node is route[len(route) - 1]:
                                logger.warning("Reached End Point")
                                flag = False
                                break

            logger.warning("Exited while loop")
            logger.info("--------------------- Distance --------------------------------")
            logger.critical("Traversing through Route : " + str(route))
            logger.critical("Total Distance covered : " + str(distance))
            logger.critical("Total Nodes covered : " + str(route_step + 1))

        except:
            logger.error("An exception occurred during calculation")

    # Below methods are used for unit testing
    def calculate_age(self, dob_year, current_year):
        return current_year - dob_year

    def calculate_stmt(self, winning_amount):
        if winning_amount > 100:
            return True
        else:
            return False
