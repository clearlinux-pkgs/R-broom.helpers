#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-broom.helpers
Version  : 1.18.0
Release  : 22
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/broom.helpers_1.18.0.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/broom.helpers_1.18.0.tar.gz
Summary  : Helpers for Model Coefficients Tibbles
Group    : Development/Tools
License  : GPL-3.0
Requires: R-broom
Requires: R-cards
Requires: R-cli
Requires: R-dplyr
Requires: R-labelled
Requires: R-lifecycle
Requires: R-purrr
Requires: R-rlang
Requires: R-stringr
Requires: R-tibble
Requires: R-tidyr
BuildRequires : R-broom
BuildRequires : R-cards
BuildRequires : R-cli
BuildRequires : R-dplyr
BuildRequires : R-labelled
BuildRequires : R-lifecycle
BuildRequires : R-purrr
BuildRequires : R-rlang
BuildRequires : R-stringr
BuildRequires : R-tibble
BuildRequires : R-tidyr
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# broom.helpers <img src="man/figures/broom.helpers.png" align="right" width="120" />

%prep
%setup -q -n broom.helpers
pushd ..
cp -a broom.helpers buildavx2
popd
pushd ..
cp -a broom.helpers buildavx512
popd
pushd ..
cp -a broom.helpers buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736300203

%install
export SOURCE_DATE_EPOCH=1736300203
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/broom.helpers/DESCRIPTION
/usr/lib64/R/library/broom.helpers/INDEX
/usr/lib64/R/library/broom.helpers/Meta/Rd.rds
/usr/lib64/R/library/broom.helpers/Meta/data.rds
/usr/lib64/R/library/broom.helpers/Meta/features.rds
/usr/lib64/R/library/broom.helpers/Meta/hsearch.rds
/usr/lib64/R/library/broom.helpers/Meta/links.rds
/usr/lib64/R/library/broom.helpers/Meta/nsInfo.rds
/usr/lib64/R/library/broom.helpers/Meta/package.rds
/usr/lib64/R/library/broom.helpers/Meta/vignette.rds
/usr/lib64/R/library/broom.helpers/NAMESPACE
/usr/lib64/R/library/broom.helpers/NEWS.md
/usr/lib64/R/library/broom.helpers/R/broom.helpers
/usr/lib64/R/library/broom.helpers/R/broom.helpers.rdb
/usr/lib64/R/library/broom.helpers/R/broom.helpers.rdx
/usr/lib64/R/library/broom.helpers/WORDLIST
/usr/lib64/R/library/broom.helpers/data/Rdata.rdb
/usr/lib64/R/library/broom.helpers/data/Rdata.rds
/usr/lib64/R/library/broom.helpers/data/Rdata.rdx
/usr/lib64/R/library/broom.helpers/doc/index.html
/usr/lib64/R/library/broom.helpers/doc/tidy.R
/usr/lib64/R/library/broom.helpers/doc/tidy.Rmd
/usr/lib64/R/library/broom.helpers/doc/tidy.html
/usr/lib64/R/library/broom.helpers/help/AnIndex
/usr/lib64/R/library/broom.helpers/help/aliases.rds
/usr/lib64/R/library/broom.helpers/help/broom.helpers.rdb
/usr/lib64/R/library/broom.helpers/help/broom.helpers.rdx
/usr/lib64/R/library/broom.helpers/help/figures/broom.helpers.png
/usr/lib64/R/library/broom.helpers/help/figures/broom.helpers.svg
/usr/lib64/R/library/broom.helpers/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/broom.helpers/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/broom.helpers/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/broom.helpers/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/broom.helpers/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/broom.helpers/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/broom.helpers/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/broom.helpers/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/broom.helpers/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/broom.helpers/help/paths.rds
/usr/lib64/R/library/broom.helpers/html/00Index.html
/usr/lib64/R/library/broom.helpers/html/R.css
/usr/lib64/R/library/broom.helpers/tests/spelling.R
/usr/lib64/R/library/broom.helpers/tests/testthat.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-add_coefficients_type.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-add_contrasts.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-add_estimate_to_reference_rows.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-add_header_rows.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-add_n.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-add_pairwise_contrasts.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-add_reference_rows.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-add_term_labels.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-add_variable_labels.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-assert_package.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-attach_and_detach.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-disambiguate_terms.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-get_response_variable.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-helpers.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-identify_variables.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-list_higher_order_variables.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-marginal_tidiers.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-model_get_n.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-remove_intercept.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-select_helpers.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-select_variables.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-tidy_parameters.R
/usr/lib64/R/library/broom.helpers/tests/testthat/test-tidy_plus_plus.R
