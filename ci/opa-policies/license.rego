package policies.license
deny[msg] {
  some i
  lic := lower(input.Packages[i].LicenseConcluded)
  lic != null
  contains(lic, "gpl")
  msg := sprintf("Policy: Disallowed license detected (%s).", [lic])
}
