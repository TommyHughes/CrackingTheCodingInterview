SELECT T.tenantid
	,T.tenantname
	,COUNT(APTNT.aptid) AS "COUNTER"
FROM tenants AS T
LEFT JOIN apttenants AS APTNT
	ON T.tenantid=APTNT.tenantid
GROUP BY T.tenantid,T.tenantname
HAVING COUNT(APTNT.aptid)>1
;