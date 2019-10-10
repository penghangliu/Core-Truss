#include "main.h"

int main (int argc, char *argv[]) {

	const auto t1 = chrono::steady_clock::now();
	if (argc < 3) {
		fprintf(stderr, "usage: %s "
				"\n <filename>"
				"\n <nucleus type: 12, 13, 14, 23, 24, 34>"
				"\n <hierarchy?: YES or NO>\n", argv[0]);
		exit(1);
	}

	char *filename = argv[1];
	string tmp (argv[1]);
	string gname = tmp.substr (tmp.find_last_of("/") + 1);

	string nd (argv[2]);
	if (!(nd == "12" || nd == "13" || nd == "14" || nd == "23" || nd == "24" || nd == "34" || nd == "11")) {
		printf ("Invalid algorithm, options are 12, 13, 14, 23, 24, and 34\n");
		exit(1);
	}

	// read the graph, give sorted edges in graph
	edge nEdge = 0;
	Graph graph;
	readGraph<vertex, edge> (filename, graph, &nEdge);
	string hrc (argv[3]);
    string vfile = "P0_result";
//    string vfile = gname + "_" + nd;
//    string vfile1 = "P3_TRU" + gname;
//    string vfile2 = "P3_TRI" + gname;
	string out_file;

	bool hierarchy = (hrc == "YES" ? true : false);
	if (hierarchy)
		out_file = vfile + "_Hierarchy";
	else
		out_file = vfile + "_K";

//    FILE* fp;
    FILE* fp = fopen (vfile.c_str(), "ab");

	vertex maxK; // maximum K value in the graph
    vertex maxk;
	vector<vertex> K;
    vector<vertex> KK;

	if (nd == "12")
		base_kcore (graph, hierarchy, nEdge, K, &maxK, vfile, fp);
	else if (nd == "13")
		base_k13 (graph, hierarchy, nEdge, K, &maxK, vfile, fp);
	else if (nd == "14")
		base_k14 (graph, hierarchy, nEdge, K, &maxK, gname, fp);
	else if (nd == "23") {
        base_ktruss (graph, hierarchy, nEdge, K, KK, &maxK, vfile, fp);
//                base_ktruss_storeTriangles (graph, hierarchy, nEdge/2, K, &maxK, vfile, fp);
	}
	else if (nd == "24")
		base_k24 (graph, hierarchy, nEdge, K, &maxK, vfile, fp);
	else if (nd == "34")
		base_k34 (graph, hierarchy, nEdge, K, &maxK, vfile, fp);
    else if (nd == "11"){
        base_kcore (graph, hierarchy, nEdge, KK, &maxk, vfile, fp);
        base_ktruss (graph, hierarchy, nEdge, K, KK, &maxK, gname, fp);
    }

//#ifdef DUMP_K
//    string kfile = "k_values";
//    FILE* kf = fopen (kfile.c_str(), "w");
//    for (vertex i = 0; i < K.size(); i++)
//        fprintf (kf, "%lld\n", K[i]);
//    fclose (kf);
//#endif
//
//    const auto t2 = chrono::steady_clock::now();
    
//    print_time (fp, "End-to-end Time: ", t2 - t1);
    fclose (fp);
//    printf("%s \t complete! \n",gname.c_str());
    printf ("%d \t %d\t %d \t %d\n", graph.size(), nEdge, maxk, maxK);
    
	return 0;
}
