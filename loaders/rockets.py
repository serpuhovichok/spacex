from loaders.abstract import AbstractLoader
from typing import List
from models import Rocket

class RocketsLoader(AbstractLoader):
    def _get_name(self) -> str:
        return "Rockets"

    def _get_query(self) -> str:
        return """
            query {
                  rockets(limit: 10, offset: 0) {
                    active
                    boosters
                    company
                    cost_per_launch
                    country
                    description
                    diameter {
                      meters
                    }
                    engines {
                      engine_loss_max
                      layout
                      number
                      propellant_1
                      propellant_2
                      thrust_sea_level {
                        kN
                      }
                      thrust_to_weight
                      thrust_vacuum {
                        kN
                      }
                      type
                      version
                    }
                    first_flight
                    first_stage {
                      burn_time_sec
                      engines
                      fuel_amount_tons
                      reusable
                      thrust_sea_level {
                        kN
                      }
                      thrust_vacuum {
                        kN
                      }
                    }
                    height {
                      meters
                    }
                    id
                    landing_legs {
                      material
                      number
                    }
                    mass {
                      kg
                    }
                    name
                    payload_weights {
                      id
                      kg
                      name
                    }
                    second_stage {
                      burn_time_sec
                      engines
                      fuel_amount_tons
                      payloads {
                        option_1
                        composite_fairing {
                          diameter {
                            meters
                          }
                          height {
                            meters
                          }
                        }
                      }
                      thrust {
                        kN
                      }
                    }
                    stages
                    success_rate_pct
                    type
                    wikipedia
                  }
                }
        """

    def __convert_engines(self, data: dict) -> dict:
        return {
            'engine_loss_max': data['engine_loss_max'],
            'layout': data['layout'],
            'number': int(data['number']),
            'propellant_1': data['propellant_1'],
            'propellant_2': data['propellant_2'],
            'thrust_sea_level_kn': float(data['thrust_sea_level']['kN']),
            'thrust_to_weight': float(data['thrust_to_weight']),
            'thrust_vacuum_kn': float(data['thrust_vacuum']['kN']),
            'type': data['type'],
            'version': data['type']
        }

    def _convert_data(self, data: dict) -> List[Rocket]:
        result = []
        for rocket in data['data']['rockets']:
            obj = Rocket()
            obj.id = rocket['id']
            obj.name = rocket['name']
            obj.type = rocket['type']
            obj.active = bool(rocket['active'])
            obj.boosters = int(rocket['boosters'])
            obj.company = rocket['company']
            obj.cost_per_launch = int(rocket['cost_per_launch'])
            obj.country = rocket['country']
            obj.description = rocket['description']
            obj.diameter_meters = float(rocket['diameter']['meters'])
            obj.height_meters = float(rocket['height']['meters'])
            obj.mass_kg = int(rocket['mass']['kg'])
            obj.engines = self.__convert_engines(rocket['engines'])
            obj.first_flight = rocket['first_flight']
            obj.stages = int(rocket['stages'])
            # костыль, так как в данных встретился null
            first_stage_burn_time_sec = rocket['first_stage']['burn_time_sec']
            obj.first_stage_burn_time_sec = int(first_stage_burn_time_sec) if first_stage_burn_time_sec else 0
            obj.first_stage_engines = int(rocket['first_stage']['engines'])
            obj.first_stage_fuel_amount_tons = float(rocket['first_stage']['fuel_amount_tons'])
            obj.first_stage_reusable = bool(rocket['first_stage']['reusable'])
            obj.first_stage_thrust_sea_level_kn = float(rocket['first_stage']['thrust_sea_level']['kN'])
            obj.first_stage_thrust_vacuum_kn = float(rocket['first_stage']['thrust_vacuum']['kN'])
            # костыль, так как в данных встретился null
            second_stage_burn_time_sec = rocket['second_stage']['burn_time_sec']
            obj.second_stage_burn_time_sec = int(second_stage_burn_time_sec) if second_stage_burn_time_sec else 0
            obj.second_stage_engines = int(rocket['second_stage']['engines'])
            obj.second_stage_fuel_amount_tons = float(rocket['second_stage']['fuel_amount_tons'])
            obj.second_stage_thrust_kn = float(rocket['second_stage']['thrust']['kN'])
            # костыль, так как в данных встретился null
            second_stage_payloads_composite_fairing_diameter_meters = rocket['second_stage']['payloads']['composite_fairing']['diameter']['meters']
            obj.second_stage_payloads_composite_fairing_diameter_meters = float(
                second_stage_payloads_composite_fairing_diameter_meters
            ) if second_stage_payloads_composite_fairing_diameter_meters else 0.0
            # костыль, так как в данных встретился null
            second_stage_payloads_composite_fairing_height_meters = rocket['second_stage']['payloads']['composite_fairing']['height']['meters']
            obj.second_stage_payloads_composite_fairing_height_meters = float(
                second_stage_payloads_composite_fairing_height_meters
            ) if second_stage_payloads_composite_fairing_height_meters else 0.0
            obj.second_stage_payloads_option_1 = rocket['second_stage']['payloads']['option_1']
            obj.success_rate_pct = int(rocket['success_rate_pct'])
            obj.landing_legs_material = rocket['landing_legs']['material']
            obj.landing_legs_number = int(rocket['landing_legs']['number'])
            obj.wikipedia = rocket['wikipedia']
            obj.payload_weights = rocket['payload_weights']

            result.append(obj)

        return result