"""Examples of vulnerability exposure analysis with pyyaml.
"""
import yaml

 def preload_for_yaml():
   with self._preloading_env() as env:
       rendered_yaml = env.get_template(filepath).render()
       data = yaml.load(rendered_yaml, Loader=yaml.FullLoader)
       if data:
           if filename in MULTI_CLASS_FILENAMES:
               for class_name in data:
                   model_identifiers[class_name] = list(
                       data[class_name].keys())
           else:
               class_name = filename[:filename.rfind('.')]
               model_identifiers[class_name] = list(data.keys())
