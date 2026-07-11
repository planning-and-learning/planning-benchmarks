;Copyright 2018 The MITRE Corporation. All rights reserved. Approved for public release. Distribution unlimited 17-2122.
; For more information on CALDERA, the automated adversary emulation system, visit https://github.com/mitre/caldera or email attack@mitre.org
; This has 2 hosts, 4 user, 2 admin per host, 1 active account per host
(define (problem p2_hosts_trial_15)
(:domain caldera)
(:requirements :typing)
(:objects
    id_ttimedelta id_batimedelta - observedtimedelta
    id_zhost id_shost - observedhost
    id_ddomaincredential id_hdomaincredential id_pdomaincredential id_ldomaincredential - observeddomaincredential
    str__alpha str__bd str__w str__patricia str__mary str__e str__i str__bh str__q str__m str__james str__john - string
    id_adomain - observeddomain
    id_bgrat id_birat - observedrat
    id_gdomainuser id_cdomainuser id_kdomainuser id_odomainuser - observeddomainuser
)
(:init
    (knows id_bgrat)
    (knows id_shost)
    (knows_property id_bgrat pexecutable)
    (knows_property id_bgrat phost)
    (knows_property id_shost pfqdn)
    (MEM_CACHED_DOMAIN_CREDS id_shost id_ddomaincredential)
    (MEM_CACHED_DOMAIN_CREDS id_zhost id_pdomaincredential)
    (MEM_DOMAIN_USER_ADMINS id_shost id_gdomainuser)
    (MEM_DOMAIN_USER_ADMINS id_shost id_kdomainuser)
    (MEM_DOMAIN_USER_ADMINS id_zhost id_cdomainuser)
    (MEM_DOMAIN_USER_ADMINS id_zhost id_odomainuser)
    (mem_hosts id_adomain id_shost)
    (mem_hosts id_adomain id_zhost)
    (prop_cred id_cdomainuser id_ddomaincredential)
    (prop_cred id_gdomainuser id_hdomaincredential)
    (prop_cred id_kdomainuser id_ldomaincredential)
    (prop_cred id_odomainuser id_pdomaincredential)
    (PROP_DOMAIN id_cdomainuser id_adomain)
    (PROP_DOMAIN id_ddomaincredential id_adomain)
    (PROP_DOMAIN id_gdomainuser id_adomain)
    (PROP_DOMAIN id_hdomaincredential id_adomain)
    (PROP_DOMAIN id_kdomainuser id_adomain)
    (PROP_DOMAIN id_ldomaincredential id_adomain)
    (PROP_DOMAIN id_odomainuser id_adomain)
    (PROP_DOMAIN id_pdomaincredential id_adomain)
    (PROP_DOMAIN id_shost id_adomain)
    (PROP_DOMAIN id_zhost id_adomain)
    (prop_elevated id_bgrat yes)
    (prop_executable id_bgrat str__bh)
    (PROP_FQDN id_shost str__w)
    (PROP_FQDN id_zhost str__bd)
    (prop_host id_batimedelta id_zhost)
    (prop_host id_bgrat id_shost)
    (prop_host id_ttimedelta id_shost)
    (PROP_PASSWORD id_ddomaincredential str__e)
    (PROP_PASSWORD id_hdomaincredential str__i)
    (PROP_PASSWORD id_ldomaincredential str__m)
    (PROP_PASSWORD id_pdomaincredential str__q)
    (PROP_USER id_ddomaincredential id_cdomainuser)
    (PROP_USER id_hdomaincredential id_gdomainuser)
    (PROP_USER id_ldomaincredential id_kdomainuser)
    (PROP_USER id_pdomaincredential id_odomainuser)
    (PROP_USERNAME id_cdomainuser str__james)
    (PROP_USERNAME id_gdomainuser str__mary)
    (PROP_USERNAME id_kdomainuser str__john)
    (PROP_USERNAME id_odomainuser str__patricia)
    (PROP_WINDOWS_DOMAIN id_adomain str__alpha)
)
(:goal
(and
    (prop_host id_birat id_zhost)
)
)
)