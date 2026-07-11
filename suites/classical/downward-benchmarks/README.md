This fork contains fixes for modelling errors in the IPC benchmark instances. The detected errors so far are not critical but the fixes can potentially improve planner performances. It is still very incomplete but we plan to provide a more in-depth analysis in the future.


# agricola-opt18-strips
## domain
- added missing requirement :numeric-fluents 
- removed unused action parameters

## problems
- added missing requirement :typing :numeric-fluents


# airport 
## domain
- removed unused predicate is-start-runway


# airport-adl
## problems
- added missing requirement :adl
- removed unused objects


# assembly
## domain 
- removed unused predicate to-be-removed


# barman
## problems
- added missing requirement :typing


# blocks (incomplete)
## problems 
- changed to lowercase


# caldera (incomplete)
## domain
- removed unused predicate PROP_TIMEDELTA PROP_DNS_DOMAIN_NAME PROP_DC PROP_HOSTNAME PROP_IS_GROUP PROP_SECONDS PROP_MICROSECONDS PROP_DNS_DOMAIN PROP_SID

# problems 
- removed unused objects
- removed unused atoms


# cavediving (incomplete)
## domain 
- added missing requirement :numeric-fluents 

## problems 
- added missing requirements :typing :action-costs :numeric-fluents


# childsnack (incomplete)
# problems 
- added missing requirement :typing


# citycar (incomplete)
## problems 
- removed unused objects