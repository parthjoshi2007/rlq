class FactSet(set):
    def by_concept(self, evaluator):
        try:
            return self._facts_by_concept
        except AttributeError:
            facts_by_concept = {}
            for fact in self:
                concept_name = evaluator.get_concept_name(fact, None)
                if concept_name in facts_by_concept:
                    raise ValueError(
                        'Duplicate concept {} in {}. Add more clauses to your '
                        'context_groupby expression to ensure only 1 fact per concept '
                        'exists in each context group or leave it as the default.'.format(
                            concept_name, type(self).__name__))
                facts_by_concept[concept_name] = fact
            self._facts_by_concept = facts_by_concept
            return self._facts_by_concept
