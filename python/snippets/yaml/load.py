"""Examples of exposure analysis with pyyaml.
"""
import yaml

def load_from_yaml(self, filepath: str, model_identifiers: Dict[str, List[str]]):
  """
  Load fixtures from the given filename
  """
  rendered_yaml = self.env.get_template(filepath).render(
      model_identifiers=model_identifiers)
  data = yaml.load(rendered_yaml, Loader=yaml.FullLoader)

  identifier_data = {}
  filename = os.path.basename(filepath)
