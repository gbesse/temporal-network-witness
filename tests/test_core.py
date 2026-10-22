import unittest,random
from temporal_network_witness import run
class DomainTests(unittest.TestCase):
 def test_impossible_witness(self):
  d={'nodes':['a','b'],'constraints':[{'from':'a','to':'b','max':2},{'from':'b','to':'a','max':-3}]};r=run(d)
  self.assertFalse(r['feasible']);self.assertEqual(sum(e['max'] for e in r['cycle']),-1)
 def test_feasible_schedule_satisfies_every_edge(self):
  rng=random.Random(42)
  for _ in range(30):
   true={str(i):rng.randrange(-20,20) for i in range(6)};edges=[{'from':a,'to':b,'max':true[b]-true[a]+rng.randrange(5)} for a in true for b in true]
   r=run({'nodes':list(true),'constraints':edges});self.assertTrue(r['feasible'])
   for e in edges:self.assertLessEqual(r['schedule'][e['to']]-r['schedule'][e['from']],e['max'])
 def test_disconnected_negative_cycle(self):
  r=run({'nodes':['a','b'],'constraints':[{'from':'b','to':'b','max':-1}]});self.assertFalse(r['feasible']);self.assertEqual(r['cycle_bound_sum'],-1)
 def test_zero_cycle_allowed(self):
  self.assertTrue(run({'nodes':['a'],'constraints':[{'from':'a','to':'a','max':0}]})['feasible'])
 def test_duplicates_rejected(self):
  with self.assertRaises(ValueError):run({'nodes':['a','a'],'constraints':[]})
 def test_unknown_endpoint_rejected(self):
  with self.assertRaises(ValueError):run({'nodes':['a'],'constraints':[{'from':'a','to':'x','max':1}]})
